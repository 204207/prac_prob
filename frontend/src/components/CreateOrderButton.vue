<template>
  <form @submit.prevent="createOrder" style="text-align: center; margin-top: 10px;">
    <button type="submit" class="btn btn-primary">Utwórz ofertę</button>
  </form>
</template>

<script>
import axios from "axios";

export default {
  name: "CreateOrderButton",
  props: ["offer"],
  methods: {
    createOrder: function() {
      if (!localStorage.getItem("token")) {
        this.$router.push("/zaloguj");
      }
      console.log(this.offer);
      const todayDate = new Date();

      let orderData = {
        performer: {
          id: 1,
          name: "BestTrans Sp z o.o",
          tax_number: "123 456 78 90",
          street: "ul. Piotrkowska 102",
          post_code: "90-010 Łódź",
          place: "Łódź",
          country: "Poland"
        },
        loading_place: {
          date: this.offer.loading_place.date,
          hour: this.offer.loading_place.hour,
          name: this.offer.loading_place.name,
          remarks: this.offer.loading_place.remarks,
          place: this.offer.loading_place.place.id
        },
        destination: {
          date: this.offer.destination.date,
          hour: this.offer.destination.hour,
          name: this.offer.destination.name,
          remarks: this.offer.destination.remarks,
          place: this.offer.destination.place.id
        },
        cargo: {
          wrapping: "palety",
          pallets_number: this.offer.pallets_number,
          additional_remarks: this.offer.additional_remarks
        },
        additional_remarks: this.offer.additional_remarks,
        price: this.offer.price,
        date:
          todayDate.getFullYear() +
          "-" +
          todayDate.getMonth() +
          1 +
          "-" +
          todayDate.getDate(),
        is_active: false,
        customer: JSON.parse(localStorage.getItem("profile"))["id"],
        offer: this.offer.id,
        driver: 1,
        vehicle: 1
      };

      axios
        .post("http://185.238.73.103:8008/api/orders/?format=json", orderData, {
          headers: {
            Authorization: "Token " + localStorage.getItem("token")
          }
        })
        .then(response => {
          this.$router.push("/zamowienia/" + response["data"]["id"]);
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>
