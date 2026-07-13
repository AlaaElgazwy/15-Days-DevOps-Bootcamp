const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send('مرحباً بك! هذا التطبيق يعمل بنجاح داخل Docker 🐳');
});


app.listen(port, '0.0.0.0', () => {
  console.log(`App is running on http://0.0.0.0:${port}`);
});