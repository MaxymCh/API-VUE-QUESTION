import { createRouter, createWebHistory } from "vue-router";
import QuestionList from "./components/QuestionList.vue";
import QuestionnaireList from "./components/QuestionnaireList.vue";

const routes = [
  { path: "/questions", component: QuestionList },
  { path: "/questionnaires", component: QuestionnaireList },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
