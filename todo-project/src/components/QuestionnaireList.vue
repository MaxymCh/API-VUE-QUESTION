<script>
import QuestionnaireItem from './QuestionnaireItem.vue'


let data = {
questionnaires: [],
title: 'Mes questionnaires',
newItem: ''
};

export default{
  components: { QuestionnaireItem },
  data() {
    return data;
    },
    methods: {
    /*
    add: function(){
        let text = this.tache.trim();
        if(text){
            this.questions.push({ title: text, checked:false, editing:false})
            this.tache = ""
        }
        
    },
    suppr($event){this.questions.splice($event, 1) // remove it from array
    },*/
    async fetchquestionnaires(){
          let response = await fetch('http://127.0.0.1:5000/quiz/api/v1.0/questionnaires/');
          this.questionnaires = await response.json();
        }
    },
    mounted(){
        this.fetchquestionnaires();
      }

  
}

// This starter template is using Vue 3 <script setup> SFCs
// Check out https://vuejs.org/api/sfc-script-setup.html#script-setup
</script>

<template>
  <link rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css"
        integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65"
        crossorigin="anonymous">
  <div class="container">
            <h2> {{ title }} </h2>
            <ol>
                
                <li v-for="(item, indexx) in questionnaires">
                    <QuestionnaireItem 
                    :questionnaire="item"
                    :index="indexx"
                    >
                    </QuestionnaireItem>  <!--@suppr="suppr($event)">-->
                </li>
            </ol>
            <!--
            <em> Ajouter une question</em>
            <input v-model="tache" type="text" @keyup.enter="add"/>
            <span class="input-group-btn">
                <button v-on:click="add()"
                class="btn btn-default"
                type="button">Ajouter</button>
            </span>-->
        </div>
      </template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

</style>
