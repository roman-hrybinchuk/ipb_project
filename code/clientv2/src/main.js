import Vue from 'vue';
import App from './App.vue';
import router from './router';
import {BootstrapVue, IconsPlugin} from 'bootstrap-vue';
import axios from 'axios';
import VueAxios from 'vue-axios';
import VueToast from 'vue-toast-notification';

// Import Bootstrap an BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'vue-toast-notification/dist/theme-sugar.css';

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

const instance = axios.create({
    baseURL: 'http://localhost:8000',
    timeout: 2000,
});

Vue.use(VueAxios, instance)
Vue.use(VueToast);

Vue.mixin({
    methods: {
        setUser: function (email, password) {
            localStorage.setItem("user-login", btoa(`${email}:${password}`));
        },
        getUser: function () {
            return localStorage.getItem("user-login");
        },
        getMe: async function () {
            const me = await this.axios.get('/users/me', {
                headers: {
                    'Authorization': `Basic ${this.getUser()}`
                }
            })
            return me.data.user;
        }

    },
})

Vue.config.productionTip = false

new Vue({
    router,
    render: h => h(App)
}).$mount('#app')
