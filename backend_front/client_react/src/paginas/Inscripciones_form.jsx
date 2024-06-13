import { useEffect, useState } from "react";
import { useForm } from "react-hook-form";
import { useNavigate, useParams } from "react-router-dom";
import { createInscripcion, deleteInscripcion, getInscripcion, updateInscripcion, getTutorAlumnos } from "../api/Inscripciones.api";
import { toast } from "react-hot-toast";

export function Inscripciones_form() {
    const {
        register,
        handleSubmit,
        formState: { errors },
        setValue,
    } = useForm();
    const navigate = useNavigate();
    const params = useParams();
    const [tutorAlumnos, setTutorAlumnos] = useState([]);

    const onSubmit = handleSubmit(async (data) => {
        if (params.id) {
            await updateInscripcion(params.id, data);
            toast.success("Inscripción Actualizada", {
                position: "bottom-right",
                style: {
                    background: "#101010",
                    color: "#fff",
                },
            });
        } else {
            await createInscripcion(data);
            toast.success("Nueva Inscripción agregada", {
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
        async function loadInscripcion() {
            if (params.id) {
                const { data } = await getInscripcion(params.id);
                setValue("tutor_alumno", data.tutor_alumno);
                setValue("ins_contrato_fecha", data.ins_contrato_fecha);
                setValue("ins_estado", data.ins_estado);
                setValue("ins_periodo", data.ins_periodo);
                setValue("nivel", data.nivel);
                setValue("ciclo", data.ciclo);
                setValue("curso", data.curso);
                setValue("turno", data.turno);
                setValue("especializacion", data.especializacion);
            }
        }
        loadInscripcion();

        async function loadTutorAlumnos() {
            const { data } = await getTutorAlumnos();
            setTutorAlumnos(data);
        }
        loadTutorAlumnos();
    }, [params.id, setValue]);

    return (
        <div className="max-w-xl mx-auto">
            <form onSubmit={onSubmit} className="bg-zinc-800 p-10 rounded-lg mt-2">
                <select
                    {...register("tutor_alumno", { required: true })}
                    className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
                >
                    <option value="">Seleccionar Tutor/Alumno</option>
                    {tutorAlumnos.map((tutorAlumno) => (
                        <option key={tutorAlumno.id} value={tutorAlumno.id}>
                            {tutorAlumno.tutor.tut_nom} {tutorAlumno.tutor.tut_ape} - {tutorAlumno.alumno.alu_nom} {tutorAlumno.alumno.alu_ape}
                        </option>
                    ))}
                </select>
                {errors.tutor_alumno && <span>Este campo es requerido</span>}

                <input
                    type="date"
                    placeholder="Fecha de Contrato"
                    {...register("ins_contrato_fecha", { required: true })}
                    className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
                />
                {errors.ins_contrato_fecha && <span>Este campo es requerido</span>}

                <select
                    {...register("ins_estado", { required: true })}
                    className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
                >
                    <option value="">Seleccionar Estado</option>
                    <option value="Pagado">Pagado</option>
                    <option value="Pendiente">Pendiente</option>
                    <option value="Inscripto">Inscripto</option>
                </select>
                {errors.ins_estado && <span>Este campo es requerido</span>}

                <input
                    type="text"
                    placeholder="Período"
                    {...register("ins_periodo", { required: true })}
                    className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
                />
                {errors.ins_periodo && <span>Este campo es requerido</span>}

                <input
                    type="text"
                    placeholder="Nivel"
                    {...register("nivel", { required: true })}
                    className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
                />
                {errors.nivel && <span>Este campo es requerido</span>}

                <input
                    type="text"
                    placeholder="Ciclo"
                    {...register("ciclo", { required: true })}
                    className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
                />
                {errors.ciclo && <span>Este campo es requerido</span>}

                <input
                    type="text"
                    placeholder="Curso"
                    {...register("curso", { required: true })}
                    className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
                />
                {errors.curso && <span>Este campo es requerido</span>}

                <input
                    type="text"
                    placeholder="Turno"
                    {...register("turno", { required: true })}
                    className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
                />
                {errors.turno && <span>Este campo es requerido</span>}

                <input
                    type="text"
                    placeholder="Especialización"
                    {...register("especializacion", { required: true })}
                    className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
                />
                {errors.especializacion && <span>Este campo es requerido</span>}

                <button className="bg-indigo-500 p-3 rounded-lg block w-full mt-3">
                    Guardar
                </button>
            </form>
            {params.id && (
                <div className="flex justify-end">
                    <button
                        className="bg-red-500 p-3 rounded-lg w-48 mt-3"
                        onClick={async () => {
                            const accepted = window.confirm("¿ESTÁS SEGURO?");
                            if (accepted) {
                                await deleteInscripcion(params.id);
                                toast.success("Inscripción Eliminada", {
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
                        Eliminar
                    </button>
                </div>
            )}
        </div>
    );
}
