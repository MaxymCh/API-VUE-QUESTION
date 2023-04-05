

<script>
export default {
  data() {
    return {
      newQuestionnaire: {
        name: '',
      },
    };
  },
  methods: {
    async addQuestionnaire() {
      const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(this.newQuestionnaire),
      };
      const response = await fetch('http://127.0.0.1:5000/quiz/api/v1.0/questionnaire/', requestOptions);
      const data = await response.json();
      this.questionnaires.push(data.questionnaire);
      this.newQuestionnaire.name = '';
    },
  },
};
</script>
<template>
  <div class="container">
    <h2>Ajouter un nouveau questionnaire</h2>

    <form @submit.prevent="addQuestionnaire">
      <div class="form-group">
        <label for="name">Titre du questionnaire :</label>
        <input type="text" class="form-control" id="name" v-model="newQuestionnaire.name" />
      </div>

      <button type="submit" class="btn btn-default">Ajouter</button>
    </form>
  </div>
</template>
