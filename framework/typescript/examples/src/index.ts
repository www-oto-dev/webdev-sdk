// This file was generated by liblab | https://liblab.com/

import { WebOtoDevSdk } from 'web-oto-dev-sdk';

(async () => {
  const webOtoDevSdk = new WebOtoDevSdk({
    apiKey: 'YOUR_API_KEY',
  });

  const { data } = await webOtoDevSdk.admin.projects();

  console.log(data);
})();
