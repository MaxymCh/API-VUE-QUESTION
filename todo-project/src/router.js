import { createRouter, createWebHistory } from "vue-router";
import QuestionList from "./components/QuestionList.vue";
import QuestionnaireList from "./components/QuestionnaireList.vue";
import CreateQuestion from "./components/CreateQuestion.vue";
import EditQuestion from "./components/EditQuestion.vue";
import CreateQuestionnaire from "./components/CreateQuestionnaire.vue";
import EditQuestionnaire from "./components/EditQuestionnaire.vue";

const routes = [
  { path: "/questions/:idQuestionnaire", name:'QuestionList', component: QuestionList},
  { path: "/", component: QuestionnaireList },
  { path: "/question/edit/:idQuestion", component: EditQuestion },
  { path: "/questionnaire/edit/:id", component: EditQuestionnaire },
  { path: "/questionnaires", component: QuestionnaireList },
  { path: '/question/add', name: 'question-add',  component: CreateQuestion,   props: true, },
  { path: '/questionnaire/add', component: CreateQuestionnaire},
];



const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
