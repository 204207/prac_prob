<template>
  <div class="orders">
    <div style="text-align: center; margin-bottom: 30px;">
      <div style="text-align: center;">
        <h1 style="text-align: center;">Zamówienia</h1>
      </div>
      <div>
        <router-link to="/zamowienia" @click.native="getAllOrders">Wszystkie</router-link> | 
        <router-link to="/zamowienia-aktywne" @click.native="getActiveOrders">Aktywne</router-link> | 
        <router-link to="/zamowienia-archiwalne" @click.native="getArchiveOrders">Archiwalne</router-link>
      </div>
    </div>
    <div v-if="orders.length > 0">
      <div class="row orders-header">
        <div class="col-sm-3">
          <span>Miejsce załadunku</span>
        </div>
        <div class="col-sm-1"></div>
        <div class="col-sm-3">
          <span>Miejsce rozładunku</span>
        </div>
        <div class="col-sm-1">
          <span>Nadwozie</span>
        </div>
        <div class="col-sm-2">
          <span>Godziny</span>
        </div>
        <div class="col-sm-2">
          <span>Cena</span>
        </div>
      </div>
    </div>
    <div v-else style="text-align: center; margin-top: 15px;">
      <h4>Brak zamówień</h4>
    </div>
    <OrderListItem v-for="order in orders" :key="order.id" v-bind:order="order"/>
  </div>
</template>

<script>
import OrderListItem from "./OrderListItem.vue";
import axios from "axios";

export default {
  data: function() {
    return {
      orders: []
    };
  },
  mounted: function() {
    if (window.location.href.endsWith("aktywne")) {
      this.getActiveOrders();
    } else if (window.location.href.endsWith("archiwalne")) {
      this.getArchiveOrders();
    } else {
      this.getAllOrders();
    }
  },
  methods: {
    getAllOrders: function() {
      axios
        .get("http://185.238.73.103:8008/api/orders/?format=json", {
          headers: { Authorization: "Token " + localStorage.getItem("token") }
        })
        .then(response => (this.orders = response["data"]));
    },
    getActiveOrders: function() {
      axios
        .get(
          "http://185.238.73.103:8008/api/orders/get_active_orders?format=json",
          {
            headers: { Authorization: "Token " + localStorage.getItem("token") }
          }
        )
        .then(response => (this.orders = response["data"]));
    },
    getArchiveOrders: function() {
      axios
        .get(
          "http://185.238.73.103:8008/api/orders/get_past_orders?format=json",
          {
            headers: { Authorization: "Token " + localStorage.getItem("token") }
          }
        )
        .then(response => (this.orders = response["data"]));
    }
  },
  components: {
    OrderListItem
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.orders-header {
  margin: 0 auto;
  text-align: center;
}
.orders {
  margin: 50px auto;
  width: 90%;
}

.router-link-exact-active {
  font-weight: bold;
}
</style>
