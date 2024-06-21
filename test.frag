#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_mouse;
uniform vec2 u_resolution;
uniform float u_time;

uniform sampler2D u_tex0;
uniform vec2 u_tex0Resolution;

uniform float alpha;

void main(void) {
  vec2 uv = gl_FragCoord.xy / u_resolution.xy;

  float Pi = 6.28318530718;

  float Directions = 10.0;
  float Quality = 2.0;
  float Size = 80.0;

  vec2 Radius = alpha * Size / u_resolution.xy;

  // Pixel colour
  vec4 Color = texture2D(u_tex0, uv);

  // Blur calculations
  for (float d = 0.0; d < Pi; d += Pi / Directions) {
    for (float i = 1.0 / Quality; i <= 1.0; i += 1.0 / Quality) {
      Color += texture2D(u_tex0, uv + vec2(cos(d), sin(d)) * Radius * i);
    }
  }

  // Output to screen
  Color /= Quality * Directions - 15.0;
  gl_FragColor = Color;
}
