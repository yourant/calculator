<style lang="scss" scoped>

.apptitle {
  font-size: 1.7rem;
  }
.navIcon{
  size: 25;
}
.navdrawer{
  margin-top: 66px;
  max-width: 240px;
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
      label="Search"
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
              <v-card v-if="hover" height="100" width="170" class="mx-auto secondary" >
                <v-list>
                  <v-list-item >
                    <v-list-item-avatar >
                      <v-img src="@/assets/avitar.jpg"></v-img>
                    </v-list-item-avatar>
                  </v-list-item>

                  <v-list-item link>
                    <v-list-item-content>
                      <v-list-item-title class="title">
                        Race
                      </v-list-item-title>
                      <v-list-item-subtitle>raceychan@gmail.com</v-list-item-subtitle>
                    </v-list-item-content>
                    <v-list-item-action>
                      <v-icon>mdi-menu-down</v-icon>
                    </v-list-item-action>
                  </v-list-item>

                      <v-divider></v-divider>

                  <v-list-item-group v-model="selectedItem" color="primary">
                  <v-list-item v-for="(item, i) in items" :key="i" link to="/login" >

                    <v-list-item-icon>
                      <v-icon v-text="item.icon"></v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>
                      <v-list-item-title v-text="item.text"></v-list-item-title>
                    </v-list-item-content>


                  </v-list-item>
                  </v-list-item-group>
                </v-list>
              </v-card>
            </v-expand-transition>
        </v-menue>
      </v-hover>

      </v-app-bar>





  <v-navigation-drawer v-model="drawer" app class="navdrawer">
    <v-list>
      <v-list-item>
        <v-list-item-icon>
          <v-icon>mdi-home</v-icon>
        </v-list-item-icon>
        <v-list-item-title>Home</v-list-item-title>
      </v-list-item>
    <v-divider></v-divider>

    <v-list-group :value="true" prepend-icon="mdi-account-circle">
    <template v-slot:activator>
    <v-list-item-title>Users</v-list-item-title>
    </template>

    <v-list-group :value="true" no-action sub-group>
      <template v-slot:activator>
        <v-list-item-content>
          <v-list-item-title>Admin</v-list-item-title>
        </v-list-item-content>
      </template>

      <v-list-item v-for="([title, icon], i) in admins" :key="i" link >
        <v-list-item-title v-text="title"></v-list-item-title>
        <v-list-item-icon>
          <v-icon v-text="icon"></v-icon>
        </v-list-item-icon>
      </v-list-item>
    </v-list-group>

    <v-list-group no-action sub-group >
      <template v-slot:activator>
        <v-list-item-content>
          <v-list-item-title>Actions</v-list-item-title>
        </v-list-item-content>
      </template>

      <v-list-item  v-for="([title, icon], i) in cruds" :key="i" link>
        <v-list-item-title v-text="title"></v-list-item-title>
        <v-list-item-icon>
          <v-icon v-text="icon"></v-icon>
        </v-list-item-icon>
      </v-list-item>
    </v-list-group>
    </v-list-group>
    </v-list>

      <v-divider></v-divider>
      <v-spacer></v-spacer>

    <v-list>

      <v-btn block text @click="drawer = false">
      <v-icon color="grey" v-html="miniDrawer ? 'chevron_right' : 'chevron_left'"></v-icon>
      Collapse
      </v-btn>

      </v-list>
  </v-navigation-drawer>

  </nav>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

@Component
export default class Nav extends Vue {
  public drawer: boolean = false;
  public items: object = [
        { text: 'My Files', icon: 'mdi-folder' },
        { text: 'Starred', icon: 'mdi-star' },
        { text: 'Recent', icon: 'mdi-history' },
      ];

  public admins: object = [
      ['Management', 'mdi-account-multiple-outline'],
      ['Settings', 'mdi-cog-outline'],
  ];
  public cruds: object = [
      ['Create', 'mdi-plus-outline'],
      ['Read', 'mdi-file-outline'],
      ['Update', 'mdi-update'],
      ['Delete', 'mdi-delete'],
  ];
}
</script>