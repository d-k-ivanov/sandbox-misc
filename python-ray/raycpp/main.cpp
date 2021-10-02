// Run `ray cpp --show-library-path` to find headers and libraries.
#include <ray/api.h>

int main(int argc, char **argv) {
  // Start Ray runtime. If you're connecting to an existing cluster, you can set
  // the `RAY_ADDRESS` env var.
  ray::Init();
  ...
}
