<style lang="scss" scoped>

.apptitle {
  font-size: 1.7rem;
  }
.navIcon{
  size: 25;
}

.navdrawer{
  margin-top: 54px;
}

.v-icon{
  color: black
}

.v-text-field{
      max-width: 220px;
}

</style>


<template>
  <nav>
    <v-app-bar flat absolute color="white" elevate-on-scroll scroll-target="#scrolling-techniques-7">
      <v-btn icon dark >
        <v-app-bar-nav-icon color="grey" @click="drawer = !drawer"></v-app-bar-nav-icon>
      </v-btn>

    <v-divider class="mx-4" vertical></v-divider>
  

    <v-app-bar-title color="success">   
      <v-btn text to="/">
        <span class="apptitle">ModernRainforest</span>
      </v-btn>
    </v-app-bar-title>


      <!-- <v-img 
      class="mx-2"
      src="https://st3.depositphotos.com/27847728/34695/v/1600/depositphotos_346956532-stock-illustration-initial-letter-logo-design-vector.jpg"
      max-height="40"
      max-width="40"
      contain
      ></v-img> -->

      <v-spacer></v-spacer>


      <v-text-field label="Search for products" class="searchbar" prepend-icon="mdi-magnify" hide-details single-line ></v-text-field>



      <v-divider class="mx-4" vertical></v-divider>

        <v-tooltip v-model="show" bottom>
          <template v-slot:activator="{ on, attrs }">
            <v-btn icon dark v-bind="attrs" v-on="on"  to="/" >
              <v-icon color="grey" >home</v-icon>
            </v-btn>
          </template>
          <span>Home</span>
        </v-tooltip>

      <v-divider class="mx-4" vertical></v-divider>

        <v-tooltip v-model="show" bottom>
          <template v-slot:activator="{ on, attrs }">
            <v-btn icon dark v-bind="attrs" v-on="on"  to="/about" >
            <v-icon color="grey">info</v-icon>
            </v-btn>
          </template>
          <span> About</span>
        </v-tooltip>

      <v-divider class="mx-4" vertical></v-divider>

        <v-tooltip v-model="show" bottom>
          <template v-slot:activator="{ on, attrs }">
            <v-btn icon dark v-bind="attrs" v-on="on"  to="/" >
              <v-icon color="grey"> mdi-cart-outline </v-icon>
            </v-btn>
          </template>
          <span> Shopping Cart </span>
        </v-tooltip>

      <v-divider class="mx-4" vertical></v-divider>



        <v-tooltip v-model="show" left>
          <template v-slot:activator="{ on, attrs }">


            <v-hover v-slot="{ hover }">
            <v-card class="mx-auto" color="grey lighten-4"  max-width="100" >
           
            <v-expand-transition>
            <div
            v-if="hover"
            class="d-flex transition-fast-in-fast-out white darken-2 v-card--reveal display-3 grey--text"
            style="height: 50%;" >
            $14.99
            </div>
            </v-expand-transition>

            <v-card-text style="position: relative;" >
            <v-btn
            color="white"
            class="white--text"
            fab
            medium

            icon
            bottom v-bind="attrs" v-on="on"  to="/login">

            <v-icon color="grey"> mdi-account </v-icon>
            </v-btn>
            </v-card-text>

            </v-card>
            </v-hover>

          </template>

          <span> Login </span>
        </v-tooltip>







      </v-app-bar>

    <v-divider ></v-divider>

    <v-navigation-drawer v-model="drawer" app class="navdrawer">
        <v-menu bottom left offset-y>
        </v-menu>

        <v-btn  to="/">Back Home</v-btn>
        <v-icon color="grey" v-html="miniDrawer ? 'chevron_right' : 'chevron_left'">Collapse</v-icon>
    </v-navigation-drawer>

  </nav>
</template>


<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';


@Component
export default class Nav extends Vue {
  public drawer: boolean = false;
}

</script>