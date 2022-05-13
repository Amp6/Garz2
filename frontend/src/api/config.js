import axios from "axios";

if (process.env.NODE_ENV !== "production")
  axios.defaults.baseURL = "http://localhost:8000";

export default axios;