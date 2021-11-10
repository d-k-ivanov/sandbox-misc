const canv = document.querySelector("canvas");
const ctx = canv.getContext("2d");
canv.width = window.innerWidth;
canv.height = window.innerHeight;
const w = canv.width;
const h = canv.height;
const background_color = "#0003";

const randomFloat = (min, max) => Math.random() * (max - min) + min;
const randomInt = (min, max) => Math.round(randomFloat(min, max));

const mouse_pos = { x: w / 2, y: h / 2 }
const objects_amount = 3000;
const objects = [];
const max_height = 5;
const dz = 0.05;
const sr = spawn_range = 1000;
const cs = color_shift = 0;
const cr = color_range = 360;

for (let i = 0; i < objects_amount; i++)
{
    objects.push({
        x: w / 2 + randomInt(-sr, sr),
        y: h / 2 + randomInt(-sr, sr),
        color: "hsla(" + randomInt(cs, cs + cr) + ",100%,50%,0.2)",
        param: (i + 1) / (objects_amount + 1) * max_height
    });
}

canv.addEventListener("mousemove", ev =>
{
    mouse_pos.x = ev.x;
    mouse_pos.y = ev.y;
}, false);

const mainInterval = setInterval(() =>
{
    drawBg();
    drawObjects();
    moveObjects();
    objects.sort((a, b) => a.param - b.param);
}, 20);

function drawBg()
{
    ctx.fillStyle = background_color;
    ctx.fillRect(0, 0, w, h);
}

function drawObjects()
{
    objects.forEach((o) =>
    {
        ctx.fillStyle = o.color;
        ctx.beginPath();
        ctx.arc((o.x - mouse_pos.x) * o.param + w / 2,
            (o.y - mouse_pos.y) * o.param + h / 2,
            15 * o.param, 0, Math.PI * 2);
        ctx.fill();
        ctx.closePath();
    });
}

function moveObjects()
{
    objects.forEach((o) =>
    {
        o.param += dz;
        if (o.param > max_height)
        {
            o.param = 0;
            o.x = w / 2 + randomInt(-sr, sr);
            o.y = h / 2 + randomInt(-sr, sr);
        }
    });
}
