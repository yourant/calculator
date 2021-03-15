<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>

<template>
  <div id="app">
    <v-app class='grey lighten-4'>
      <Nav> </Nav> 
        <v-content v-if="loggedIn===null">
          <v-container fill-height>
            <v-row align-center justify-center>
              <v-col>
                <div class="text-xs-center">
                  <div class="headline my-5">Loading...</div>
                    <v-progress-circular size="100" indeterminate color="primary"></v-progress-circular>
                  </div>
                </v-col>
              </v-row>
            </v-container>
          </v-content>
        <router-view v-else />
      <NotificationsManager></NotificationsManager>
    </v-app>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import NotificationsManager from './components/partials/NotificationsManager.vue';
import Nav from './components/partials/Nav.vue';
import { readIsLoggedIn } from './store/main/getters';
import { dispatchCheckLoggedIn } from './store/main/actions';


@Component({
  components: {
    NotificationsManager,
    Nav,
  },
})
export default class App extends Vue {

  get loggedIn() {
    return readIsLoggedIn(this.$store);
  }

  public async created() {
    await dispatchCheckLoggedIn(this.$store);
  }
}
</script>
