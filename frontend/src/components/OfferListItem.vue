<template>
  <router-link :to="/oferty/ + offer.id" class="offer-item">
    <div class="row offers">
      <div class="col-sm-3">
        <span>{{ offer.loading_place.place.country }}</span>
        <br>
        <span>{{ offer.loading_place.place.place }}</span>
      </div>
      <div class="col-sm-1">
        <i class="fas fa-arrow-right"></i>
      </div>
      <div class="col-sm-3">
        <span>{{ offer.destination.place.country }}</span>
        <br>
        <span>{{ offer.destination.place.place }}</span>
      </div>
      <div class="col-sm-1">
        <span>{{ offer.vehicle }}</span>
      </div>
      <div class="col-sm-2">
        <span>{{ offer.loading_place.date }}</span><br/>
        <i class="fas fa-arrow-down"></i><br/>
        <span>{{ offer.destination.date }}</span>
      </div>
      <div class="col-sm-2">
        <span>{{ offer.price }} PLN</span>
      </div>
    </div>
  </router-link>
</template>

<script>
import moment from "moment";

export default {
  props: ["offer"],
  mounted: function() {
    this.offer.loading_place.date = moment(
      String(this.offer.loading_place.date)
    ).format("DD-MM-YYYY hh:mm");
    this.offer.destination.date = moment(
      String(this.offer.destination.date)
    ).format("DD-MM-YYYY hh:mm");
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.offers {
  flex-grow: 1;
  align-items: center;
  text-align: center;
}

.offers > div {
  align-content: center;
}

.offer-item {
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

.offer-item:hover {
  background-color: #e0e0f9;
}
</style>
