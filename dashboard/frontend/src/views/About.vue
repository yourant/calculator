<style lang="scss" scoped>
  .v-card {
    width: 800px;
  }
  .introduction {
    margin-top: 200px;
  }
</style>


<template>
  <v-container  class="About" >
    <v-row  justify="center" align="center" >  
      <v-col cols="12" md="6">
        <v-card class="introduction" elevation="2">
          <v-card-title>About this Website</v-card-title>
          <v-card-text>
          Hi.there! This is Cheng Chen. I graduated in the September of 2020 from the University of Californai Irvine, with my degree of B.S and a major in Mathmatics</p>
            <p class="org-description is-size-4"> 
            </p>
            <p>

            </p>
            <p>
            </p>

            <p>
            </p>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <v-row justify="center" align="center" >  
      <v-col cols="12" md="6" >
      <v-textarea solo name="input-7-4" label="leave your comment here"></v-textarea>
      </v-col>
    </v-row>

    <v-row  justify="center" align="center" > 
      <v-card flat tile class="indigo lighten-1 white--text text-center" >


  <v-dialog v-model="dialog" width="500" >
    <template v-slot:activator="{ on, attrs }">
      <v-card-text>
        <v-btn dark v-bind="attrs" v-on="on" v-for="icon in icons"  :key="icon" class="mx-4 white--text" icon >
          <v-icon size="24px"> {{ icon }} </v-icon>
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
        <v-btn color="primary" text @click="dialog = false">
        Ok
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>

        <v-card-text class="white--text pt-0">

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