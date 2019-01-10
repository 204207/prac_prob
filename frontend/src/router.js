import Vue from "vue";
import Router from "vue-router";
import HomePage from "./views/HomePage";
import OfferDetailsPage from "./views/OfferDetailsPage";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    { path: "/", component: HomePage },
    { path: "/oferty/*", component: OfferDetailsPage },

    { path: "*", component: HomePage }
  ]
});
