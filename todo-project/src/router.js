import { createRouter, createWebHistory } from "vue-router";
import QuestionList from "./components/QuestionList.vue";
import QuestionnaireList from "./components/QuestionnaireList.vue";
import CreateQuestion from "./components/CreateQuestion.vue";

const routes = [
  { path: "/questions/:idQuestionnaire", component: QuestionList },
  { path: "/questionnaires", component: QuestionnaireList },
  { path: "/question/add", component: CreateQuestion },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
