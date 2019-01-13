<template>
  <router-link :to="/zamowienia/ + order.id" class="order-item">
    <div class="row orders">
      <div class="col-sm-3">
        <span>{{ order.loading_place.place.country }}</span>
        <br>
        <span>{{ order.loading_place.place.place }}</span>
      </div>
      <div class="col-sm-1">
        <i class="fas fa-arrow-right"></i>
      </div>
      <div class="col-sm-3">
        <span>{{ order.destination.place.country }}</span>
        <br>
        <span>{{ order.destination.place.place }}</span>
      </div>
      <div class="col-sm-1">
        <span>{{ order.vehicle }}</span>
      </div>
      <div class="col-sm-2">
        <span>{{ order.loading_place.date }}</span><br/>
        <i class="fas fa-arrow-down"></i><br/>
        <span>{{ order.destination.date }}</span>
      </div>
      <div class="col-sm-2">
        <span>{{ order.price }} PLN</span>
      </div>
    </div>
  </router-link>
</template>

<script>
import moment from "moment";

export default {
  props: ["order"],
  mounted: function() {
    this.order.loading_place.date = moment(
      String(this.order.loading_place.date)
    ).format("DD-MM-YYYY hh:mm");
    this.order.destination.date = moment(
      String(this.order.destination.date)
    ).format("DD-MM-YYYY hh:mm");
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.orders {
  flex-grow: 1;
  align-items: center;
  text-align: center;
}

.orders > div {
  align-content: center;
}

.order-item {
  height: 80px;
  text-decoration: none;
  color: inherit;
  display: flex;
  align-items: center;
  flex-wrap: nowrap;
  justify-content: space-evenly;
  background-color: #e0e0e0;
  border: 1px solid grey;
  border-radius: 5px;
  margin: 5px;
}

.order-item:hover {
  background-color: #e0e0f9;
}
</style>
