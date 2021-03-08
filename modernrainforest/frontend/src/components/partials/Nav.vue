<style lang="scss" scoped>

.apptitle {
  font-size: 1.7rem;
  }
.navIcon{
  size: 25;
}
.navdrawer{
  margin-top: 66px;
}
.v-icon{
  color: black
}
.v-text-field{
      max-width: 220px;
}
.theme--light.v-divider {
    border-color: rgba(0,0,0,0.12) !important; 

}
</style>


<template>
  <nav>
    <v-app-bar fixed absolute  color="white" scroll-target="#scrolling-techniques-7">
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



    <v-autocomplete
      v-model="select"
      :loading="loading"
      :items="items"
      :search-input.sync="search"
      prepend-icon="mdi-magnify"
      cache-items
      class="mx-4"
      flat
      hide-no-data
      hide-details
      label="What product do you like?"
      solo-inverted
    ></v-autocomplete>
    <v-btn icon>
      <v-icon>mdi-dots-vertical</v-icon>
    </v-btn>


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

      <v-hover v-slot="{ hover }" >
        <v-menue class="mx-auto"   max-width="100" >
          <v-icon color="grey"> mdi-account </v-icon>
            <v-expand-transition>
              <v-card v-if="hover" height="100" width="100" class="mx-auto secondary" >
                <v-list>
                  <v-list-item v-for="list in lists" :key="list" link to="/login" >
                    <v-list-item-title v-text="list"></v-list-item-title>
                  </v-list-item>
                </v-list>
              </v-card>
            </v-expand-transition>
        </v-menue>
      </v-hover>

      </v-app-bar>



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
  public lists: object = [
        'LOGIN',
        'PROFILE',
        'HISTORY',
      ];
}
</script>