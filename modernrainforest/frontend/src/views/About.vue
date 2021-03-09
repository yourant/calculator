<style lang="scss" scoped>
  .v-card {
    margin-top: 150px;
    max-width: 800px;
  }
</style>


<template>
  <v-container  class="About" >
    <v-row  justify="center" align="center" >  
      <v-col cols="12" md="6">
        <v-card elevation="2">
          <v-card-title>About this Website</v-card-title>
          <v-card-text>
          Hi.there! This is Cheng Chen. I graduated in the September of 2020 from the University of Californai Irvine, with my degree of B.S and a major in Mathmatics</p>
            <p class="org-description is-size-4"> 
            as I have been self-learning programming(frontend,backend and ML), I think it would be a good idea to build something that involves several developing philosophy 
            like separation of front-end and backend, microservices, stateless along the way, </p>
            <p>and that is why you would see the website you are visiting right now.</p>
            <p>The plan I have in mind right now is to build this to be a e-commerce website,
            mainly selling merchandizes that I have crash on. </p>

            <p>The website is built under the help of great techniques such as
            Vue,Vuex,Vuetify, Fastapi, Postgresql, Elastic Search, Redis, Traefik, Celery, Pytorch, Docker, Kubernetes and etc.
            Send a message to RaceyChan if you are interested in such field and would like to communicate, or just to say hi ;) 
            </p>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <v-row  justify="center" align="center" >  
      <v-col cols="12" md="6"> 
      <v-textarea solo name="input-7-4" label="leave your comment here"></v-textarea>
      </v-col>
    </v-row>

    <v-row  justify="center" align="center" > 
      <v-card flat tile class="indigo lighten-1 white--text text-center" >


  <v-dialog v-model="dialog" width="500" >

    <template v-slot:activator="{ on, attrs }">

        <v-card-text>
          <v-btn dark v-bind="attrs" v-on="on" v-for="icon in icons"  :key="icon" class="mx-4 white--text" icon >
          <v-icon size="24px">
            {{ icon }}
          </v-icon>
          </v-btn>
        </v-card-text>

    </template>

    <v-card>
      <v-card-title class="headline grey lighten-2">
      Contact Info
      </v-card-title>
        <v-card-text>
          wechat:DreamAlreadyGone
        </v-card-text>

      <v-divider></v-divider>

        <v-card-actions>
        <v-spacer></v-spacer>
          <v-btn color="primary" text @click="dialog = false" >
            Ok
          </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>

        <v-card-text class="white--text pt-0">
          Hi.there! This is Cheng Chen. I graduated in the September of 2020 from the University of Californai Irvine,
          with my degree of B.S and a major in Mathmatics
          i will leave my contact at the top so you would you able to reach out to me anytime you like!
        </v-card-text>


        <v-divider></v-divider>
        <v-card-text class="white--text">
        {{ new Date().getFullYear() }} — <strong>Race</strong>
        </v-card-text>
      </v-card>
    </v-row>

  </v-container>
</template>



<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
@Component

export default class About extends Vue {
  public dialog: boolean = false;
  public icons: object = [
        'mdi-facebook',
        'mdi-twitter',
        'mdi-linkedin',
        'mdi-instagram',
        ];
}
</script>