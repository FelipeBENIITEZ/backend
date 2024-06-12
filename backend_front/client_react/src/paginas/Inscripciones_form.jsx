import { useEffect } from "react";
import { useForm } from "react-hook-form";
import { useNavigate, useParams } from "react-router-dom";
import { createInscripcion, deleteInscripcion, getAllInscripciones, getInscripcion, updateInscripcion } from "../api/Inscripciones.api";
import { toast } from "react-hot-toast";
export function Inscripciones_form(){
    const {
        register,
        handleSubmit,
        formState: { errors },
        setValue,
      } = useForm();
      const navigate = useNavigate();
      const params = useParams();
    
      const onSubmit = handleSubmit(async (data) => {
        if (params.id) {
          await updateInscripcion(params.id, data);
          toast.success("Inscripcion Actualizada", {
            position: "bottom-right",
            style: {
              background: "#101010",
              color: "#fff",
            },
          });
        } else {
          await createInscripcion(data);
          toast.success("Nueva Inscripcion agregada", {
            position: "bottom-right",
            style: {
              background: "#101010",
              color: "#fff",
            },
          });
        }
    
        navigate("/Inscripciones");
      });
    
      useEffect(() => {
        async function loadInscripciones() {
          if (params.id) {
            const { data } = await getInscripcion(params.id);
            setValue("NOMBRE", data.title);
            setValue("Descripcion", data.description);
          }
        }
        loadInscripciones();
      }, []);
    
      return (
        <div className="max-w-xl mx-auto">
          <form onSubmit={onSubmit} className="bg-zinc-800 p-10 rounded-lg mt-2">
            <input
              type="text"
              placeholder="Alumno"
              {...register("NOMBRE", { required: true })}
              className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
              autoFocus
            />
    
            {errors.title && <span>This field is required</span>}
    
            <textarea
              placeholder="Descripcion"
              {...register("DESCRIPCION", { required: true })}
              className="bg-zinc-700 p-3 rounded-lg block w-full"
            />
    
            {errors.description && <span>This field is required</span>}
    
            <button className="bg-indigo-500 p-3 rounded-lg block w-full mt-3">
              Save
            </button>
          </form>
    
          {params.id && (
            <div className="flex justify-end">
              <button
                className="bg-red-500 p-3 rounded-lg w-48 mt-3"
                onClick={async () => {
                  const accepted = window.confirm("ESTAS SEGURO?");
                  if (accepted) {
                    await deleteInscripcion(params.id);
                    toast.success("Inscripcion Eliminada", {
                      position: "bottom-right",
                      style: {
                        background: "#101010",
                        color: "#fff",
                      },
                    });
                    navigate("/Inscripciones");
                  }
                }}
              >
                delete
              </button>
            </div>
          )}
        </div>
      );
}