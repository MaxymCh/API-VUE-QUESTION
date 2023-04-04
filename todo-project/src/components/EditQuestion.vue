<script>
import { useRoute } from "vue-router"
import { onMounted } from 'vue';
export default {
  data() {
    return {
      question: "",
      reponses_question: "",
      title: 'Editer Question',

    };
  },
  methods: {
    async edit() {
      var data_body = {
          'title': this.question.title,
          'type': this.question.question_type,
          'firstAlternative': this.reponses_question.firstAlternative,
          'secondAlternative': this.reponses_question.secondAlternative
        }
      if(this.question.question_type == "MultipleQuestion"){
        data_body.thirdAlternative = this.reponses_question.thirdAlternative 
        data_body.fourthAlternative = this.reponses_question.fourthAlternative
      }
       
      const requestOptions = {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        
        body: JSON.stringify(data_body),
      };
      const response = await fetch(`http://127.0.0.1:5000/quiz/api/v1.0/question/${this.question.id}`, requestOptions).then(response => response.json());

    },
    async fetchquestion(idQuestion){
          let response = await fetch(`http://127.0.0.1:5000/quiz/api/v1.0/question/${idQuestion}`);
          this.question = await response.json();
        },
    async fetchreponses(idQuestion){
          let response = await fetch(`http://127.0.0.1:5000/quiz/api/v1.0/question/reponse/${idQuestion}`);
          this.reponses_question = await response.json();
        }
},

mounted(){
      const route = useRoute();
      this.idQuestion = route.params.idQuestion;
      this.fetchquestion(this.idQuestion);
      this.fetchreponses(this.idQuestion);
    }
};
</script><template>
  <div class="container">
    <h2>{{ title }}</h2>

    <form @submit.prevent="edit">
      <div class="form-group">
        <label for="title">Titre</label>
        <input type="text" class="form-control" id="title" v-model="question.title" />
      </div>
      <div class="form-group">
        <label for="type">Type de question:</label>
        <select class="form-control" id="type" v-model="question.question_type">
          <option value="SimpleQuestion">Question simple</option>
          <option value="MultipleQuestion">Question à choix multiples</option>
        </select>
      </div>
      <div class="form-group">
        <label for="firstAlternative">Première alternative:</label>
        <input type="text" class="form-control" id="firstAlternative" v-model="reponses_question.firstAlternative" />
      </div>
      
      <div class="form-group">
        <label for="secondAlternative">Deuxième alternative:</label>
        <input type="text" class="form-control" id="secondAlternative" v-model="reponses_question.secondAlternative" />
      </div>
      
      <div v-if="question.question_type === 'MultipleQuestion'" class="form-group">
        <label for="thirdAlternative">Troisième alternative:</label>
        <input type="text" class="form-control" id="thirdAlternative" v-model="reponses_question.thirdAlternative" />
      </div>
      
      <div v-if="question.question_type === 'MultipleQuestion'" class="form-group">
        <label for="fourthAlternative">Quatrième alternative:</label>
        <input type="text" class="form-control" id="fourthAlternative" v-model="reponses_question.fourthAlternative" />
      </div>
    


  <button type="submit" class="btn btn-default">Modifier</button>
</form>

  </div>
</template>