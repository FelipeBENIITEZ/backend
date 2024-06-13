import React from "react";
import { useNavigate } from "react-router-dom";

export function Inscripcion_card({ inscripcion }) {
  const navigate = useNavigate();

  const tutorAlumno = inscripcion.tutor_alumno;
  const alumno = tutorAlumno?.alumno;
  const tutor = tutorAlumno?.tutor;

  return (
    <div
      className="bg-zinc-800 p-3 hover:bg-zinc-700 hover:cursor-pointer"
      onClick={() => {
        navigate(`/inscripciones/${inscripcion.id}`);
      }}
    >
      <h1 className="text-white font-bold uppercase rounded-lg">
        {alumno ? `${alumno.alum_nom} ${alumno.alum_ape}` : "Datos del alumno no disponibles"}
      </h1>
      <p className="text-slate-400">Fecha de Contrato: {inscripcion.ins_contrato_fecha}</p>
      <p className="text-slate-400">Estado: {inscripcion.ins_estado}</p>
      <p className="text-slate-400">Período: {inscripcion.ins_periodo}</p>
      <p className="text-slate-400">Tutor: {tutor ? `${tutor.tut_nom} ${tutor.tut_ape}` : "Datos del tutor no disponibles"}</p>
    </div>
  );
}
