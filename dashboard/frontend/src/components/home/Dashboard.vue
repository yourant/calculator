<style lang="scss" scoped>
    .v-card {
        margin-top: 100px;
    }

</style>





<template>
<div>
<v-container>

<v-card class="pa-md-4 mx-lg-auto text-center" max-width="1200">

<v-card-text class="display-1 font-weight-thin">
傲基 2.0品类排名看板
</v-card-text>

<v-row>
    <v-col cols="6" >
        <v-autocomplete 
        v-model="value"
        :items="items"
        dense
        prepend-icon="mdi-menu-open"
        outlined
        label="选择品类"
        ></v-autocomplete>
    </v-col>
    <v-col cols="6" >
       <v-menu ref="menu" v-model="menu" :close-on-content-click="false"
        :return-value.sync="date" transition="scale-transition" offset-y
        max-width="290px" min-width="auto">
        <template v-slot:activator="{ on, attrs }">
          <v-text-field v-model="date" label="选择日期" prepend-icon="mdi-calendar"
            readonly outlined dense
            v-bind="attrs" v-on="on" >
          </v-text-field>
        </template>
        <v-date-picker v-model="date" type="month">

          <v-spacer></v-spacer>
          <v-btn text color="primary" @click="menu = false" >
            Cancel
          </v-btn>
          <v-btn text color="primary" @click="$refs.menu.save(date)" >
            OK
          </v-btn>
        </v-date-picker>
      </v-menu>
    </v-col>
</v-row>



<v-card-text>
    <v-row> 
        <v-col span='6'>   
            <v-card-title>
                <v-text-field 
                v-model="search"
                append-icon="mdi-magnify"
                label="ASIN搜索"
                single-line hide-details >
                </v-text-field>
            </v-card-title>

            <v-data-table :headers="catnames"
                @on-row-click="showDetail"
                :items="catdata"
                :search="search" loading
                loading-text="加载中... 请稍候">
            </v-data-table>    
        </v-col>


        <v-col span='3'>  
            <div ref="chart" style="width: 900px;height:590px "> </div>
        </v-col> 
    </v-row>
</v-card-text>

    <v-divider></v-divider>

    <v-card-actions class="justify-center">
      <v-btn  text >
       导出数据
      </v-btn>
    </v-card-actions>
  </v-card>

</v-container>
</div>
</template>



<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

@Component
export default class Dashboard extends Vue {
    public date: string = new Date().toISOString().substr(0, 7);
    public menu: boolean = false;


}
</script>
