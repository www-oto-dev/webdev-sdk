#!/bin/sh


# SPECIAL: Mike's Studio
if [ -f ~/.zshenv ]; then
	. ~/.zshenv
fi

# Building library with liblab
#liblab build


# Replace 'framework'
if [ -d "$PWD"/output ]; then

	# Patching output
	from='print("before_request")'; to=''
	sed -i -e "s/$from/$to/g" "$PWD"/output/python/src/web_oto_dev_sdk/hooks/hook.py

	from='print("after_response")'; to='pass'
	sed -i -e "s/$from/$to/g" "$PWD"/output/python/src/web_oto_dev_sdk/hooks/hook.py

	from='print("on_error")'; to='pass'
	sed -i -e "s/$from/$to/g" "$PWD"/output/python/src/web_oto_dev_sdk/hooks/hook.py

	from='bash'; to='sh'
	sed -i -e "s/$from/$to/g" "$PWD"/output/python/install.sh

	if [ -d "$PWD"/framework ]; then
		rm -fR "$PWD"/framework
	fi

	mv "$PWD"/output "$PWD"/framework

fi




# Building & installing
cd "$PWD"/framework/python/
pip install build
python -m build --outdir dist .
pip install dist/web_oto_dev_sdk-1.0.1-py3-none-any.whl --force-reinstall
cd ../..



