<script>
import TodoItem from './QuestionItem.vue';

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
  methods: {
    async add() {
      const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(this.newQuestion),
      };
      const response = await fetch('http://127.0.0.1:5000/quiz/api/v1.0/question/', requestOptions);
      const data = await response.json();
      this.questions.push(data.questionnaire);
      this.newQuestion.title = '';
      this.newQuestion.type = 'SimpleQuestion';
      this.newQuestion.firstAlternative = '';
      this.newQuestion.secondAlternative = '';
      this.newQuestion.thirdAlternative = '';
      this.newQuestion.fourthAlternative = '';
    },
    async suppr(index) {
      const questionId = this.questions[index].id;
      this.questions.splice(index, 1);
      const response = await fetch(`http://127.0.0.1:5000/quiz/api/v1.0/question/${questionId}`, {
        method: 'DELETE',
      });
      const result = await response.json();
      if (!result.result) {
        console.error('Erreur lors de la suppression de la question.');
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
};
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
