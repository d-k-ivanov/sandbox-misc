// Run `ray cpp --show-library-path` to find headers and libraries.
#include <ray/api.h>

// A regular C++ function.
int MyFunction()
{
    return 1;
}

int SlowFunction()
{
    std::this_thread::sleep_for(std::chrono::seconds(10));
    return 1;
}

static int FunctionWithAnArgument(int value)
{
    return value + 1;
}

int main(int argc, char **argv)
{
    // Start Ray runtime. If you're connecting to an existing cluster, you can set
    // the `RAY_ADDRESS` env var.
    RayConfig config;
    config.num_cpus = 8;
    config.num_gpus = 4;
    config.resources = {{"Custom", 2}};
    // ray::Init();
    ray::Init(config);

    // Register as a remote function by `RAY_REMOTE`.
    RAY_REMOTE(MyFunction);

    // Invoke the above method as a Ray remote function.
    // This will immediately return an object ref (a future) and then create
    // a task that will be executed on a worker process.
    auto res = ray::Task(MyFunction).Remote();

    // The result can be retrieved with ``ray::ObjectRef::Get``.
    assert(*res.Get() == 1);

    RAY_REMOTE(SlowFunction);

    // Invocations of Ray remote functions happen in parallel.
    // All computation is performed in the background, driven by Ray's internal event loop.
    for (int i = 0; i < 4; i++)
    {
        // This doesn't block.
        ray::Task(SlowFunction).Remote();
    }

    RAY_REMOTE(FunctionWithAnArgument);

    auto obj_ref1 = ray::Task(MyFunction).Remote();
    assert(*obj_ref1.Get() == 1);

    // You can pass an object ref as an argument to another Ray remote function.
    auto obj_ref2 = ray::Task(FunctionWithAnArgument).Remote(obj_ref1);
    assert(*obj_ref2.Get() == 2);
}
