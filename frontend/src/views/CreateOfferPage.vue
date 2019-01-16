<template>
  <div>
    <Navbar/>
    <div class="container" style="margin-top: 30px;">
      <div class="section-container leading-place">
        <h4>Dane odbioru</h4>
        <form>
          <div class="form-row">
            <div class="form-group col-md-3">
              <label for="inputDate">Data</label>
              <input
                type="datetime-local"
                class="form-control"
                id="inputDate"
                v-model="loadingDate"
              >
            </div>
            <div class="form-group col-md-9">
              <label for="inputAdditionalInfo">Dodatkowe informacje</label>
              <input
                type="text"
                class="form-control"
                id="inputAdditionalInfo"
                v-model="loadingAdditionalInfo"
              >
            </div>
          </div>
          <div class="form-row">
            <div class="form-group col-md-4">
              <label for="inputStreet">Ulica</label>
              <input type="text" class="form-control" id="inputStreet" v-model="loadingStreet">
            </div>
            <div class="form-group col-md-3">
              <label for="inputCity">Miejscowość</label>
              <input type="text" class="form-control" id="inputCity" v-model="loadingCity">
            </div>
            <div class="form-group col-md-2">
              <label for="inputPostalCode">Kod pocztowy</label>
              <input
                type="text"
                class="form-control"
                id="inputPostalCode"
                v-model="loadingPostalCode"
              >
            </div>
            <div class="form-group col-md-3">
              <label for="inputCountry">Kraj</label>
              <input type="text" class="form-control" id="inputCountry" v-model="loadingCountry">
            </div>
          </div>
        </form>
      </div>
      <div class="section-container destination-place">
        <h4>Dane dostarczenia</h4>
        <form>
          <div class="form-row">
            <div class="form-group col-md-3">
              <label for="inputDate">Data</label>
              <input
                type="datetime-local"
                class="form-control"
                id="inputDate"
                v-model="destinationDate"
              >
            </div>
            <div class="form-group col-md-9">
              <label for="inputAdditionalInfo">Dodatkowe informacje</label>
              <input
                type="text"
                class="form-control"
                id="inputAdditionalInfo"
                v-model="destinationAdditionalInfo"
              >
            </div>
          </div>
          <div class="form-row">
            <div class="form-group col-md-4">
              <label for="inputStreet">Ulica</label>
              <input type="text" class="form-control" id="inputStreet" v-model="destinationStreet">
            </div>
            <div class="form-group col-md-3">
              <label for="inputCity">Miejscowość</label>
              <input type="text" class="form-control" id="inputCity" v-model="destinationCity">
            </div>
            <div class="form-group col-md-2">
              <label for="inputPostalCode">Kod pocztowy</label>
              <input
                type="text"
                class="form-control"
                id="inputPostalCode"
                v-model="destinationPostalCode"
              >
            </div>
            <div class="form-group col-md-3">
              <label for="inputCountry">Kraj</label>
              <input
                type="text"
                class="form-control"
                id="inputCountry"
                v-model="destinationCountry"
              >
            </div>
          </div>
        </form>
      </div>
      <div class="section-container details" style="height: 150px;">
        <h4>Szczegóły</h4>
        <form>
          <div class="form-row">
            <div class="form-group col-md-2">
              <label for="inputPrice">Oferowana cena</label>
              <input type="number" class="form-control" id="inputPrice" v-model="price">
            </div>
            <div class="form-group col-md-2">
              <label for="inputPaletNumber">Ilość palet</label>
              <input type="number" class="form-control" id="inputPaletNumber" v-model="palletsNum">
            </div>
            <div class="form-group col-md-8">
              <label for="inputAdditionalRemarks">Dodatkowe uwagi</label>
              <input
                type="text"
                class="form-control"
                id="inputAdditionalRemarks"
                v-model="additionalInfo"
              >
            </div>
          </div>
        </form>
      </div>
      <form @submit.prevent="createOffer" style="text-align: center; margin-top: 10px;">
        <button type="submit" class="btn btn-primary">Utwórz ofertę</button>
      </form>
    </div>
    <Footer v-if="false" />
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import Footer from "@/components/Footer.vue";
import axios from "axios";

export default {
  name: "CreateOfferPage",
  data() {
    return {
      loadingCountry: "",
      loadingCity: "",
      loadingPostalCode: "",
      loadingStreet: "",
      loadingDate: new Date(),
      loadingAdditionalInfo: "",
      destinationCountry: "",
      destinationCity: "",
      destinationPostalCode: "",
      destinationStreet: "",
      destinationDate: "",
      destinationAdditionalInfo: "",
      price: null,
      palletsNum: null,
      additionalInfo: ""
    };
  },
  mounted: function() {
    if (!localStorage.getItem("token")) {
      this.$router.push("/zaloguj");
    }
  },
  methods: {
    createOffer: function() {
      let offerData = {
        name: "Nazwa",
        additional_remarks: this.additionalInfo,
        price: parseFloat(this.price),
        pallets_number: parseInt(this.palletsNum),
        is_active: false,
        vehicle: 1,
        loading_place: {
          date: this.loadingDate,
          hour: "00:00",
          name: "Nazwa",
          remarks: this.loadingAdditionalInfo,
          place: {
            street: this.loadingStreet,
            post_code: this.loadingPostalCode,
            place: this.loadingCity,
            country: this.loadingCountry
          }
        },
        destination: {
          date: this.loadingDate,
          hour: "00:00",
          name: "Nazwa",
          remarks: this.loadingAdditionalInfo,
          place: {
            street: this.loadingStreet,
            post_code: this.loadingPostalCode,
            place: this.loadingCity,
            country: this.loadingCountry
          }
        }
      };

      axios
        .post("http://185.238.73.103:8008/api/offers/?format=json", offerData, {
          headers: {
            Authorization: "Token " + localStorage.getItem("token")
          }
        })
        .then(response => {
          this.$router.push("/oferty/" + response["data"]["id"]);
        })
        .catch(error => {
          console.log(error);
        });
    }
  },
  components: {
    Navbar,
    Footer
  }
};
</script>

<style scoped>
form {
  padding: 15px;
}

.section-container {
  padding: 10px;
  margin: 0 auto;
  margin-bottom: 10px;
  width: 80%;
  height: 250px;
  background-color: #e0e0e0;
  display: block;
  border-radius: 5px;
}

input[type="datetime-local"]::-webkit-clear-button {
  display: none;
}
</style>
