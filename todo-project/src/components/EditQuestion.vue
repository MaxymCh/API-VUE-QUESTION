<script>
import { useRoute } from "vue-router"
import { onMounted } from 'vue';
export default {
  data() {
    return {
      questions: [],
      title: 'Editer Question',
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

},
mounted(){
      const route = useRoute();
      this.idQuestion = route.params.idQuestion
    }
};
</script><template>
  <div class="container">
    <h2>{{ title }}</h2>

    <form @submit.prevent="add">
      <div class="form-group">
        <label for="title">Titre:</label>
        <input type="text" class="form-control" id="title" v-model="newQuestion.title" />
      </div>
      <div class="form-group">
        <label for="type">Type de question:</label>
        <select class="form-control" id="type" v-model="newQuestion.type">
          <option value="SimpleQuestion">Question simple</option>
          <option value="MultipleQuestion">Question à choix multiples</option>
        </select>
      </div>
      <div v-if="newQuestion.type === 'SimpleQuestion'" class="form-group">
        <label for="firstAlternative">Première alternative:</label>
        <input type="text" class="form-control" id="firstAlternative" v-model="newQuestion.firstAlternative" />
      </div>
      <div v-if="newQuestion.type === 'SimpleQuestion'" class="form-group">
        <label for="secondAlternative">Deuxième alternative:</label>
        <input type="text" class="form-control" id="secondAlternative" v-model="newQuestion.secondAlternative" />
      </div>
      <div v-if="newQuestion.type === 'MultipleQuestion'" class="form-group">
        <label for="firstAlternative">Première alternative:</label>
        <input type="text" class="form-control" id="firstAlternative" v-model="newQuestion.firstAlternative" />
      </div>
      <div v-if="newQuestion.type === 'MultipleQuestion'" class="form-group">
        <label for="secondAlternative">Deuxième alternative:</label>
        <input type="text" class="form-control" id="secondAlternative" v-model="newQuestion.secondAlternative" />
</div>
      <div v-if="newQuestion.type === 'MultipleQuestion'" class="form-group">
        <label for="thirdAlternative">Troisième alternative:</label>
        <input type="text" class="form-control" id="thirdAlternative" v-model="newQuestion.thirdAlternative" />
      </div>
      <div v-if="newQuestion.type === 'MultipleQuestion'" class="form-group">
        <label for="fourthAlternative">Quatrième alternative:</label>
        <input type="text" class="form-control" id="fourthAlternative" v-model="newQuestion.fourthAlternative" />
      </div>



  <button type="submit" class="btn btn-default">Ajouter</button>
</form>

  </div>
</template>