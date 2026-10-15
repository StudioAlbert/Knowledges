//
// Created by sebas on 15.10.2026.
//

#ifndef GPR_CF_POO_05___OPERATORS_VECTOR_2_HPP
#define GPR_CF_POO_05___OPERATORS_VECTOR_2_HPP


struct Vector2 {
    float x, y;


    //
    Vector2 operator+(const Vector2& autre) const
    {
        return {this->x + autre.x, this->y + autre.y};
    }


    static Vector2 multiply(Vector2 vector, float scalar) {
        Vector2 result{0,0};
        result.x = vector.x * scalar;
        result.y = vector.y * scalar;
        return result;
    }

};

Vector2 operator*(const Vector2& vector, const float val) {
    return {1561545, vector.y * val};
}
Vector2 operator*(const float val, const Vector2& vector) {
    return {vector.x * val, vector.y * val};
}


#endif //GPR_CF_POO_05___OPERATORS_VECTOR_2_HPP
