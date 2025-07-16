const axios = require('axios');

axios.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
  .then(response => 
console.log(`Bitcoin price: $${response.data.bitcoin.usd}`))
  .catch(error => 
    console.error('Error fetching data:', error));

