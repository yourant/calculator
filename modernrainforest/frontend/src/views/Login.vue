<style lang="scss" scoped>

</style>




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


            <v-card-text> 
                <v-form @keyup.enter="submit">
                  <v-text-field @keyup.enter="submit" v-model="email" prepend-icon="person" name="login" label="Login" type="text"></v-text-field>
                  <v-text-field @keyup.enter="submit" v-model="password" prepend-icon="lock" name="password" label="Password" id="password" type="password"></v-text-field>
                </v-form>
                <div v-if="loginError">
                  <v-alert :value="loginError" transition="fade-transition" type="error">
                    Incorrect email or password
                  </v-alert>
                </div>
                <v-col class="caption text-xs-right"><router-link to="/recover-password">Forgot your password?</router-link></v-col>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn class="ma-2" color="orange darken-2" dark to="/register">Register
                              <v-icon dark left> mdi-arrow-up </v-icon>
                    </v-btn>



                  <v-btn @click.prevent="submit" color='primary'> Login
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
import { Component, Vue } from 'vue-property-decorator';
import { api } from '@/api';
import { appName } from '@/env';
import { readLoginError } from '@/store/main/getters';
import { dispatchLogIn } from '@/store/main/actions';


@Component
export default class Login extends Vue {
  // Original ,stored in store, global var
  public email: string = '';
  public password: string = '';
  public appName = appName;
  // end

  public get loginError() {
    return readLoginError(this.$store);
  }
  public submit() {
    dispatchLogIn(this.$store, {username: this.email, password: this.password});
  }
}
</script>
