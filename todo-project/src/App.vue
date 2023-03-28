<script>
import TodoItem from './components/TodoItem.vue'


let data = {
questions: [],
title: 'Mes questions',
newItem: ''
};

export default{
  components: { TodoItem },
  data() {
    return data;
    },
    methods: {
    add: function(){
        let text = this.tache.trim();
        if(text){
            this.questions.push({ title: text, checked:false, editing:false})
            this.tache = ""
        }
        
    },
    suppr($event){this.questions.splice($event, 1) // remove it from array
    },
    async fetchquestions(){
          let response = await fetch('https://jsonplaceholder.typicode.com/questions/');
          this.questions = await response.json();
        }
    },
    mounted(){
        this.fetchquestions();
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
                
                <li v-for="(item, indexx) in questions">
                    <TodoItem 
                    :todo="item"
                    :index="indexx"
                    @suppr="suppr($event)">
                    
                </TodoItem> 
                </li>
            </ol>
            <em> Ajouter une question</em>
            <input v-model="tache" type="text" @keyup.enter="add"/>
            <span class="input-group-btn">
                <button v-on:click="add()"
                class="btn btn-default"
                type="button">Ajouter</button>
            </span>
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
