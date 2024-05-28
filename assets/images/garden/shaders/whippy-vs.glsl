#ifdef GL_ES
#define LOWP lowp
#define MEDP mediump
#define HIGP highp
#else
#define LOWP
#define MEDP
#define HIGP
#endif

attribute vec4 a_position;
attribute vec3 a_normal;
attribute MEDP vec2 a_texCoord0;
attribute vec3 a_wind;

uniform mat3 u_normal;
uniform mat4 u_projView;

varying LOWP float intensity;
varying MEDP vec2 texCoords;

void main() {
 //	vec3 n = normalize(u_normal * a_normal);
 	//vec3 l = normalize(vec3(1, 1, -1));
    //intensity = max(dot(n, l), 0.0);
    
    vec4 addon = vec4(a_position.y*a_wind.x,a_position.y*a_wind.y, a_position.y*a_wind.z, 0);
    
	texCoords = a_texCoord0;
	gl_Position = u_projView * (a_position + addon);
	
	
	//texCoords = a_texCoord0;
	//gl_Position = u_projView * a_position;
}
