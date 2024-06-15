import axios from 'axios';

const API_URL = 'http://localhost:8000/api/v1/inscripciones/inscripciones/';
const API_TUTOR_ALUMNOS_URL = 'http://127.0.0.1:8000/api/v1/tutores/tutor_alumnos/';
const API_ARANCEL_URL= 'http://127.0.0.1:8000/api/v1/inscripciones/aranceles/';
export const getAllInscripciones = async () => {
  return await axios.get(`${API_URL}`);
};

export const getInscripcion = async (id) => {
  return await axios.get(`${API_URL}/${id}`);
};

export const createInscripcion = async (inscripcion) => {
  return await axios.post(API_URL, inscripcion);
};

export const updateInscripcion = async (id, inscripcion) => {
  return await axios.put(`${API_URL}/${id}`, inscripcion);
};

export const deleteInscripcion = async (id) => {
  return await axios.delete(`${API_URL}/${id}`);
};

export const getTutorAlumnos = async () => {
  return await axios.get(API_TUTOR_ALUMNOS_URL);
};
export const getAllAranceles = async () => {
  return await axios.get(`${API_ARANCEL_URL}`);
};
export const getArancel = async (id) => {
  return await axios.get(`${API_ARANCEL_URL}/${id}`);
};
export const createArancel = async (arancel) => {
  return await axios.post(API_ARANCEL_URL, arancel);
};

export const updateArancel = async (id, arancel) => {
  return await axios.put(`${API__ARANCEL_URL}/${id}`, arancel);
};

export const deleteArancel = async (id) => {
  return await axios.delete(`${API__ARANCEL_URL}/${id}`);
};