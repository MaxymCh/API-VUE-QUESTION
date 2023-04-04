import { createRouter, createWebHistory } from "vue-router";
import QuestionList from "./components/QuestionList.vue";
import QuestionnaireList from "./components/QuestionnaireList.vue";
import CreateQuestion from "./components/CreateQuestion.vue";
import EditQuestion from "./components/EditQuestion.vue";

const routes = [
  { path: "/questions/:idQuestionnaire", component: QuestionList },
  { path: "/", component: QuestionnaireList },
  { path: "/question/edit/:idQuestion", component: EditQuestion },
  { path: "/questionnaires", component: QuestionnaireList },
  { path: '/question/add', name: 'question-add',  component: CreateQuestion,   props: true, },
];



const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
