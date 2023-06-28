import { route } from 'quasar/wrappers';
import {
  createMemoryHistory,
  createRouter,
  createWebHashHistory,
  createWebHistory,
} from 'vue-router';
import { api } from 'boot/axios';
import { Cookies } from 'quasar';

import routes from './routes';

/*
 * If not building with SSR mode, you can
 * directly export the Router instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Router instance.
 */

export default route(function (/* { store, ssrContext } */) {
  const createHistory = process.env.SERVER
    ? createMemoryHistory
    : (process.env.VUE_ROUTER_MODE === 'history' ? createWebHistory : createWebHashHistory);

  const Router = createRouter({
    scrollBehavior: () => ({ left: 0, top: 0 }),
    routes,

    // Leave this as is and make changes in quasar.conf.js instead!
    // quasar.conf.js -> build -> vueRouterMode
    // quasar.conf.js -> build -> publicPath
    history: createHistory(process.env.VUE_ROUTER_BASE),
  });

  Router.beforeEach(async (to) => {
    const publicPages = ['/login'];
    const authRequired = !publicPages.includes(to.path);
    let auth = false;
    if(Cookies.has('user_info')){
      const user_info: Record<string,string> = Cookies.get('user_info')
      console.log(user_info.token)
      if(user_info.token){
        const res = await api.get('/auth/validate', {headers: {Authorization: `Bearer ${user_info.token}`}} );
        auth = res.status == 200
      }
    }
    if (authRequired && !auth) {
        return '/login';
    }
  });
  
  return Router;  
});

