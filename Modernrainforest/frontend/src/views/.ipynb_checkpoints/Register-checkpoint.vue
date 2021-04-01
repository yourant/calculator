<template>
    <v-card-text >
            <v-container>

          <v-form v-model="valid" ref="form" lazy-validation>
            <v-text-field label="Full Name" v-model="fullName" required></v-text-field>
            <v-text-field label="E-mail" type="email" v-model="email" v-validate="'required|email'" data-vv-name="email" :error-messages="errors.collect('email')" required></v-text-field>


            <v-layout align-center>
              <v-flex>
                <v-text-field type="password" ref="password" label="Set Password" data-vv-name="password" data-vv-delay="100" v-validate="{required: true}" v-model="password1" :error-messages="errors.first('password')">
                </v-text-field>
                <v-text-field type="password" label="Confirm Password" data-vv-name="password_confirmation" data-vv-delay="100" data-vv-as="password" v-validate="{required: true, confirmed: 'password'}" v-model="password2" :error-messages="errors.first('password_confirmation')">
                </v-text-field>
              </v-flex>
            </v-layout>
          </v-form>

            <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn @click="cancel">Cancel</v-btn>
            <v-btn @click.prevent="submit">Submit</v-btn>
            </v-card-actions>
            </v-container>
        </v-card-text>
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