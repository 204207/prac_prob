import Vue from "vue";
import Router from "vue-router";
import HomePage from "./views/HomePage";
import OfferDetailsPage from "./views/OfferDetailsPage";
import LoginPage from "./views/LoginPage";
import RegisterPage from "./views/RegisterPage";
import OrdersPage from "./views/OrdersPage";
import LogoutPage from "./views/LogoutPage";
import AboutUsPage from "./views/AboutUsPage";
import CreateOfferPage from "./views/CreateOfferPage";

Vue.use(Router);

export const router = new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    { path: "/", component: HomePage },
    { path: "/oferty/*", component: OfferDetailsPage },
    { path: "/o-nas", component: AboutUsPage },
    { path: "/stworz-oferte", component: CreateOfferPage },

    { path: "/zaloguj", component: LoginPage },
    { path: "/zarejestruj", component: RegisterPage },
    { path: "/wyloguj", component: LogoutPage },

    { path: "/zamowienia", component: OrdersPage },

    { path: "*", component: HomePage }
  ]
});

router.beforeEach((to, from, next) => {
  const privatePages = ["/zamowienia", "/wyloguj"];
  const authRequired = privatePages.includes(to.path);
  const loggedIn = localStorage.getItem("token");

  if (authRequired && !loggedIn) {
    return next("/zaloguj");
  }

  next();
});

export default router;
