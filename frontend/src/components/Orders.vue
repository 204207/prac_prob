<template>
  <div>
    <div v-if="orders.length > 0">
      <ul>
        <li v-for="order in orders" :key="order.id">{{ order.id }}</li>
      </ul>
    </div>
    <div v-else>
      <h2>Brak zamówień</h2>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data: function() {
    return {
      orders: []
    };
  },
  mounted: function() {
    axios
      .get("http://185.238.73.103:8008/api/orders/?format=json", {
        headers: { Authorization: "Token " + localStorage.getItem("token") }
      })
      .then(response => (this.orders = response["data"]));
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.offers {
  margin: 0 auto;
  width: 90%;
}
</style>
