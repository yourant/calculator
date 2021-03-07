<template>

  <v-content>
          <v-container fluid fill-height>
          <v-row justify="center" align="center" >
            <v-col xs="12" sm="8" md="4">
                <v-card class="elevation-12">
                <v-toolbar dark color="primary">
                  <v-col>
                  <v-toolbar-title>{{appName}}</v-toolbar-title>
                  </v-col>
                <v-spacer></v-spacer>
                </v-toolbar>

                <v-card-text >
                    <v-form v-model="valid" ref="form" lazy-validation>
                      <v-text-field label="Full Name" v-model="fullName" required></v-text-field>
                      <v-text-field label="E-mail" type="email" v-model="email" v-validate="'required|email'" data-vv-name="email" :error-messages="errors.collect('email')" required></v-text-field>

                        <v-col>
                          <v-text-field type="password" ref="password" label="Set Password" data-vv-name="password" data-vv-delay="100" v-validate="{required: true}" v-model="password1" :error-messages="errors.first('password')">
                          </v-text-field>
                          <v-text-field type="password" label="Confirm Password" data-vv-name="password_confirmation" data-vv-delay="100" data-vv-as="password" v-validate="{required: true, confirmed: 'password'}" v-model="password2" :error-messages="errors.first('password_confirmation')">
                          </v-text-field>
                        </v-col>
                    </v-form>
                    <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn class="ma-2" color="orange darken-2" dark @click="cancel">Cancel
                      <v-icon dark left> mdi-arrow-left </v-icon>
                    </v-btn>
                   
                    <v-btn @click.prevent="submit" color='primary'>Submit         
                      <v-icon dark right > mdi-checkbox-marked-circle </v-icon>
                    </v-btn>
                    </v-card-actions>
                </v-card-text>
                </v-card>
              </v-col>
            </v-row>
            </v-container>
  </v-content>
</template>


<script lang="ts">

import {
  IUserProfileUpdate,
  IUserProfileRegister,
} from '@/interfaces';
import { Component, Vue } from 'vue-property-decorator';
import { appName } from '@/env';
import { dispatchSetNewUser } from '@/store/main/actions';

@Component
export default class Register extends Vue {
  public valid = true;
  public email: string = '';
  public fullName: string = '';
  public password1: string = '';
  public password2: string = '';
  public isActive: boolean = true;
  public appName = appName;
  public cancel() {
    this.$router.back();
  }

  public async submit() {
    if (await this.$validator.validateAll()) {
      const updatedProfile: IUserProfileRegister = {
        email: this.email,
      };
      if (this.fullName) {
        updatedProfile.full_name = this.fullName;
      }
      if (this.email) {
        updatedProfile.email = this.email;
      }
      updatedProfile.password = this.password1;
      await dispatchSetNewUser(this.$store, updatedProfile);
      this.$router.push('/login');
    }
  }
}

</script>


<style>
</style>