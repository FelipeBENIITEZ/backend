import { useNavigate } from "react-router-dom";

export function Inscripcion_card({ inscripcion }) {
  const navigate = useNavigate();

  return (
    <div
      className="bg-zinc-800 p-3 hover:bg-zinc-700 hover:cursor-pointer"
      onClick={() => {
        navigate(`/inscripciones/${inscripcion.id}`);
      }}
    >
      <h1 className="text-white font-bold uppercase rounded-lg">
        {inscripcion.title}
      </h1>
      <p className="text-slate-400">{inscripcion.description}</p>
    </div>
  );
}