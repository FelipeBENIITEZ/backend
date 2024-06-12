import axios from "axios";

const URL =
  process.env.NODE_ENV === "production"
    ? import.meta.env.VITE_BACKEND_URL
    : "http://localhost:8000";

const InscripcionesApi = axios.create({
  baseURL: `${URL}/apiinscripciones/api/v1/inscripciones`,
});

export const getAllInscripciones = () => InscripcionesApi.get("/");

export const getInscripcion = (id) => InscripcionesApi.get(`/${id}`);

export const createInscripcion = (Inscripciones) => InscripcionesApi.post("/", Inscripciones);

export const updateInscripcion = (id, Inscripciones) => InscripcionesApi.put(`/${id}/`, Inscripciones);

export const deleteInscripcion = (id) => InscripcionesApi.delete(`/${id}`);
