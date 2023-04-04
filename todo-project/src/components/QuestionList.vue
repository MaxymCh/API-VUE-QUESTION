<script>
import TodoItem from './QuestionItem.vue'
import { useRoute } from "vue-router"
import { onMounted } from 'vue';


let data = {
questions: [],
title: 'Mes questions',
newItem: '',
id: '',
};


export default {
  components: { TodoItem },
  data() {
    return {
      questions: [],
      title: 'Mes questions',
      newQuestion: {
        title: '',
        type: 'SimpleQuestion',
        firstAlternative: '',
        secondAlternative: '',
        thirdAlternative: '',
        fourthAlternative: '',
      },
    };
  },

    /*
  setup(){
   
    onMounted(() => {
      
    })
  },*/
  methods: {
  suppr: async function(index) {
    // Récupérer l'ID de la question à supprimer
    const questionId = this.questions[index].id;

    // Supprimer la question de la liste locale
    this.questions.splice(index, 1);

    // Envoyer une requête DELETE au serveur
    const response = await fetch(`http://127.0.0.1:5000/quiz/api/v1.0/question/${questionId}`, {
      method: 'DELETE',
    });

    // Vérifier si la suppression a réussi
    const result = await response.json();
    if (!result.result) {
      console.error("Erreur lors de la suppression de la question.");
    }
    
  },async fetchquestions(idQuestionnaire){
          let response = await fetch(`http://127.0.0.1:5000/quiz/api/v1.0/questionnaire/questions/${idQuestionnaire}`);
          this.questions = await response.json();
        }
    },
  mounted(){
    const route = useRoute();
    this.id = route.params.idQuestionnaire
    this.fetchquestions(this.id);
  }
}

/*
    add: function(){
        let text = this.tache.trim();
        if(text){
            this.questions.push({ title: text, checked:false, editing:false})
            this.tache = ""
        }
        
    },
    async fetchquestions() {
      const response = await fetch('http://127.0.0.1:5000/quiz/api/v1.0/questions/');
      this.questions = await response.json();
    },
  },
  mounted() {
    this.fetchquestions();
  },
};*/
</script>

<template>
  <link rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css"
        integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65"
        crossorigin="anonymous">
  <div class="container">
            <h2> {{ title }} </h2>
            <p> id  {{ id }} </p>
            <ol>
                
                <li v-for="(item, indexx) in questions">
                  <TodoItem
                  :question="item"
                  :index="indexx"
                  @suppr="suppr($event)"
                ></TodoItem>
                </li>
            </ol>
            <span class="input-group-btn">
  <router-link to="/question/add" class="btn btn-default">Ajouter une question</router-link>
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
