import { createApp } from 'vue'
import App from './App.vue'

var cors = require('cors')

const app = createApp(App);
app.use(cors);
app.mount('#app');
