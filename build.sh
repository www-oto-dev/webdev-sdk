#!/bin/sh


# SPECIAL: Mike's Studio
if [ -f ~/.zshenv ]; then
	. ~/.zshenv
fi



# Installing lates version of liblab
#sudo npm update -g liblab

# Building library with liblab
#liblab build


# Increment version in pyproject.toml (patch version)
pyproject="$PWD/framework/python/pyproject.toml"
if [ -f "$pyproject" ]; then
	current_version=$(grep -E '^version = "[0-9]+\.[0-9]+\.[0-9]+"' "$pyproject" | sed 's/version = "\(.*\)"/\1/')
	if [ -n "$current_version" ]; then
		major=$(echo "$current_version" | cut -d. -f1)
		minor=$(echo "$current_version" | cut -d. -f2)
		patch=$(echo "$current_version" | cut -d. -f3)
		new_patch=$((patch + 1))
		new_version="$major.$minor.$new_patch"
		sed -i '' "s/version = \"$current_version\"/version = \"$new_version\"/" "$pyproject"
		echo "Version incremented: $current_version -> $new_version"
	fi
fi


# Replace 'framework'
if [ -d "$PWD"/output ]; then


	# Replacing Hook file
	rm -f "$PWD/output/python/src/web_oto_dev_sdk/hooks/hook.py" && \
	cp "$PWD/hooks/python/src/hook.py" "$PWD/output/python/src/web_oto_dev_sdk/hooks/hook.py"

	# Patching output
	
	#from='print("before_request")'; to=''
	#sed -i -e "s/$from/$to/g" "$PWD"/output/python/src/web_oto_dev_sdk/hooks/hook.py
	#
	#from='print("after_response")'; to='pass'
	#sed -i -e "s/$from/$to/g" "$PWD"/output/python/src/web_oto_dev_sdk/hooks/hook.py
	#
	#from='print("on_error")'; to='pass'
	#sed -i -e "s/$from/$to/g" "$PWD"/output/python/src/web_oto_dev_sdk/hooks/hook.py


	from='bash'; to='sh'
	sed -i -e "s/$from/$to/g" "$PWD"/output/python/install.sh

	if [ -d "$PWD"/framework ]; then
		rm -fR "$PWD"/framework
	fi






	# Copy sdk_wrapper.py в output (to support sdk.crm.deals.new())
	cp "$PWD"/sdk_wrapper.py "$PWD"/output/python/src/web_oto_dev_sdk/sdk_wrapper.py


	# Патчим __init__.py
	init_file="$PWD"/output/python/src/web_oto_dev_sdk/__init__.py
	cp "$init_file" "$init_file.bak"

	sed -i '' 's/from \.client import WebOtoDevSdk/from .client import WebOtoDevSdk as _WebOtoDevSdk/g' "$init_file"

	sed -i '' 's/from \.sdk import WebOtoDevSdk/from .sdk import WebOtoDevSdk as _WebOtoDevSdk/g' "$init_file"

	cat <<EOF >> "$init_file"

from .sdk_wrapper import SDKWrapper

def WebOtoDevSdk(*args, **kwargs):
    return SDKWrapper(_WebOtoDevSdk(*args, **kwargs))
EOF





	# OUTPUT -> FRAMEWORK
	if [ -d "$PWD"/framework ]; then
		rm -fR "$PWD"/framework
	fi	
	mv "$PWD"/output "$PWD"/framework

fi



# Building & installing
cd "$PWD"/framework/python/
pip install build
python -m build --outdir dist .
# Get version from pyproject.toml
VERSION=$(grep -E '^version = "[0-9]+\.[0-9]+\.[0-9]+"' pyproject.toml | sed 's/version = "\(.*\)"/\1/')
pip install "dist/web_oto_dev_sdk-${VERSION}-py3-none-any.whl" --force-reinstall
cd ../..


# Publishing
pip install twine
cd "$PWD"/framework/python/
VERSION=$(grep -E '^version = "[0-9]+\.[0-9]+\.[0-9]+"' pyproject.toml | sed 's/version = "\(.*\)"/\1/')
python3 -m twine upload "dist/web_oto_dev_sdk-${VERSION}-py3-none-any.whl"
cd ../..