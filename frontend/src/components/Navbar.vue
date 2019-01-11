<template>
  <nav class="navbar navbar-expand-sm navbar-dark bg-dark justify-content-end">
    <div class="container">
      <a class="navbar-brand mb-0 h1" href="/">Best Trans</a>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <router-link class="nav-link" to="/">Strona główna</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/o-nas">O nas</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/zamowienia" v-if="isLoggedIn">Moje zamówienia</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/stworz-oferte">Stwórz ofertę</router-link>
          </li>
        </ul>
        <div class="ml-auto">
          <router-link to="/wyloguj" v-if="isLoggedIn">
            <button class="btn btn-secondary ml-auto">Wyloguj</button>
          </router-link>
          <router-link to="/zaloguj" v-if="!isLoggedIn">
            <button class="btn btn-success ml-auto" style="margin-right: 10px;">Zaloguj</button>
          </router-link>
          <router-link to="/zarejestruj" v-if="!isLoggedIn">
            <button class="btn btn-warning ml-auto">Zarejestruj</button>
          </router-link>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  data: function() {
    return {
      isLoggedIn: false
    };
  },
  mounted: function() {
    this.isLoggedIn = localStorage.getItem("token");
    const url = window.location;

    Array.from(document.getElementsByClassName("nav-link")).forEach(element => {
      element.classList.remove("active");
      if (url.toString() === element.href.toString()) {
        element.classList.add("active");
      }
    });
  }
};
</script>
