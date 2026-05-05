using LinearAlgebra

# Ejercicio 3

function son_ortogonales(a::Vector{Float64}, b::Vector{Float64})::Bool
    p = dot(a, b)
    return abs(p) <= eps(Float64)
end

function son_paralelos(a::Vector{Float64}, b::Vector{Float64})::Bool
    p = dot(a, b)
    cos_theta = p / (norm(a) * norm(b))
    return abs(abs(cos_theta) - 1) <= eps(Float64)
end

function identificar_vectores(a::Vector{Float64}, b::Vector{Float64})::Nothing
    if son_ortogonales(a, b)
        println("Son ortogonales")
        return
    end
    if son_paralelos(a, b)
        println("Son paralelos/antiparalelos")
        return
    end
    println("No son ni ortogonales ni paralelos/antiparalelos")
end

a = [1.0, 2.0]
b = -3 .* a
c = [-2.0, 1.0]
d = [1.0, 3.0]

identificar_vectores(a, b)
identificar_vectores(a, c)
identificar_vectores(b, c)
identificar_vectores(c, d)
