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

    suppr: async function(index) {
    // Récupérer l'ID de la question à supprimer
    const questionnaireId = this.questionnaires[index].id;

    // Supprimer la question de la liste locale
    this.questionnaires.splice(index, 1);

    // Envoyer une requête DELETE au serveur
    const response = await fetch(`http://127.0.0.1:5000/quiz/api/v1.0/questionnaire/${questionnaireId}`, {
      method: 'DELETE',
    });

    // Vérifier si la suppression a réussi
    const result = await response.json();
    if (!result.result) {
      console.error("Erreur lors de la suppression de la question.");
    }},
    
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
                    @suppr="suppr($event)"
                    >
                    </QuestionnaireItem>
                </li>
            </ol>

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

.container {
  background-color: #f8f9fa;
  border-radius: 10px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.checkbox {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #fff;
  border: 1px solid #dee2e6;
  border-radius: 5px;
  padding: 10px;
  width: 100%;
}

.checkbox > div {
  flex-basis: 100%;
  margin-bottom: 10px;
}

h2 {
  color: #6c757d;
}

ol {
  list-style: none;
  padding-left: 0;
}

li {
  margin-bottom: 10px;
}



.btn-danger {
  background-color: #dc3545;
  border-color: #dc3545;
  margin-left: 10px;
}

.btn-danger:hover {
  background-color: #c82333;
  border-color: #bd2130;
}

.btn-primary {
  background-color: #007bff;
  border-color: #007bff;
}

.btn-primary:hover {
  background-color: #0069d9;
  border-color: #0062cc;
}

a {
  color: #007bff;
  text-decoration: none;
}

a:hover {
  color: #0056b3;
  text-decoration: underline;
}

.btn-group {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-end;
  margin-left: 10px;
}

.btn-group button {
  margin: 5px 0;
}

</style>
