
<script>
import { useRoute } from "vue-router";

export default {
  data() {
    return {
      questionnaire: {
        id: "",
        name: "",
      },
    };
  },
  methods: {
    async editName() {
      const requestOptions = {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name: this.questionnaire.name }),
      };
      const response = await fetch(
        `http://127.0.0.1:5000/quiz/api/v1.0/questionnaire/${this.questionnaire.id}`,
        requestOptions
      ).then((response) => response.json());
      this.$router.push('/');
    },
    async fetchQuestionnaire(id) {
      let response = await fetch(
        `http://127.0.0.1:5000/quiz/api/v1.0/questionnaire/${id}`
      );
      this.questionnaire = await response.json();
    },
  },
  mounted() {
    const route = useRoute();
    this.questionnaire.id = route.params.id;
    this.fetchQuestionnaire(this.questionnaire.id);
  },
};
</script>

<template>
  <div class="container">
    <h2>Éditer le nom du questionnaire</h2>
    <form @submit.prevent="editName">
      <div class="form-group">
        <label for="name">Nom</label>
        <input type="text" class="form-control" id="name" v-model="questionnaire.name" />
      </div>
      <button type="submit" class="btn btn-default">Modifier</button>
    </form>
  </div>
</template>
